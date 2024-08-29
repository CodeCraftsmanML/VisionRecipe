from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import requests
import gradio as gr
import warnings

warnings.filterwarnings('ignore')

# Load the pre-trained Vision Transformer model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

api_key = 'kkfeuVW+o1JaWjIseIlS1w==elTGGRhLieoKMkxQ'  # Securely manage your API key

def identify_image(image_path):
    """Identify the food item in the image."""
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]
    food_name = predicted_label.split(',')[0]
    return food_name

def get_recipe(food_name):
    """Get the recipe information of the identified food item."""
    api_url = f'https://api.api-ninjas.com/v1/recipe?query={food_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    
    if response.status_code == requests.codes.ok:
        recipe = response.json()
    else:
        recipe = {"Error": response.status_code, "Message": response.text}
    
    return recipe

def format_recipe_info(recipe_data):
    """Format the recipe data into HTML format."""
    if not recipe_data or isinstance(recipe_data, dict) and "Error" in recipe_data:
        return "<p>No recipe information found.</p>"

    # Check if recipe_data is a list or a single recipe
    if isinstance(recipe_data, list):
        recipes = recipe_data
    else:
        recipes = [recipe_data]
    
    output = ""
    
    for recipe in recipes:
        # Recipe Title
        output += f"<h2>Recipe Name: {recipe.get('title', 'Unknown')}</h2>\n"
        
        # Servings
        servings = recipe.get('servings', 'Unknown')
        output += f"<p><strong>Servings:</strong> {servings}</p>\n"
        
        # Ingredients
        ingredients = recipe.get('ingredients', '')
        output += "<h3>Ingredients:</h3>\n<ul>\n"
        ingredient_list = ingredients.split('|')
        for ingredient in ingredient_list:
            output += f"<li>{ingredient.strip()}</li>\n"
        output += "</ul>\n"
        
        # Instructions
        instructions = recipe.get('instructions', '')
        output += "<h3>Instructions:</h3>\n<ol>\n"
        instruction_list = instructions.split('. ')
        for instruction in instruction_list:
            if instruction.strip():  # Avoid adding empty steps
                output += f"<li>{instruction.strip()}.</li>\n"
        output += "</ol>\n"
        
        output += "<hr>\n"  # Separator between recipes

    return output

def main_process(image_path):
    """Identify the food item and fetch its recipe information."""
    food_name = identify_image(image_path)
    recipe_info = get_recipe(food_name)
    formatted_recipe_info = format_recipe_info(recipe_info)
    return formatted_recipe_info

def gradio_interface(image):
    """Interface function for Gradio."""
    formatted_recipe_info = main_process(image)
    return formatted_recipe_info

# Create the Gradio UI
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Image(type="filepath"),
    outputs="html",  # Changed to HTML for proper display
    title="Food Recipe Info",
    description="Upload an image of food to get recipe information.",
    allow_flagging="never"  # Disable flagging
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
