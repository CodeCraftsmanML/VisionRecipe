# VisionRecipe

## Introduction

In this project, I’ve developed a web application named **VisionRecipe** that utilizes computer vision techniques to generate recipes from photos of food items. By leveraging Hugging Face's vision models and large language models (LLM), the application provides users with a seamless way to discover recipes based on the food they have.

## User Interaction

When you visit the VisionRecipe web application, you’ll be prompted to upload a clear image of a food item. The application processes the uploaded photo to identify the food and suggest possible recipes.

## Image Processing

Once the photo is uploaded, the application begins processing the image using advanced computer vision techniques. This involves analyzing the food item to determine its characteristics and ingredients.

## Recipe Generation

After the image analysis, the application utilizes a model from Hugging Face, which is based on transformers and autoregressive models, to generate a relevant recipe. This recipe includes ingredients and cooking instructions tailored to the identified food item.

## Data Extraction and Integration

The application fetches additional information and enhances the recipe generation using the API from API-Ninjas, ensuring comprehensive and accurate recipe suggestions.

## Error Handling

If the application is unable to identify the food item or generate a recipe, it will halt the process and inform the user of the issue, ensuring a smooth user experience.

This project showcases an innovative approach to culinary exploration by combining image recognition with recipe generation, making it a fun and practical tool for cooking enthusiasts.

Feel free to explore the application and see how it transforms your food images into delicious recipes!

## Techniques Used

- **Computer Vision**: Hugging Face vision models for food identification.
- **Transformers**: Utilizing autoregressive models for recipe generation.
- **API Integration**: Fetching additional recipe data from API-Ninjas.
- **Web Interface**: Developed using Gradio for user interaction.

## Installation

Instructions for setting up the development environment and installing dependencies:

```bash
pip install -r requirements.txt

Usage
To use the web application, including uploading food images:
bash


gradio app.py
Technical Details
Libraries Installed: Gradio, Hugging Face Transformers, API-Ninjas SDK, OpenCV
Error Handling and Configuration: The application employs robust error handling mechanisms to ensure smooth operation and user guidance.
License
This project is licensed under the MIT License.
Contact Information
For any questions or suggestions, please contact:
Email: karanmakwana@gmail.com
GitHub: https://github.com/CodeCraftsmanML
