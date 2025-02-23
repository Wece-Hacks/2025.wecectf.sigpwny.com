from PIL import Image


# IMPLEMENT THE EXTRACT_LSB FUNCTION
def extract_lsb(image_path):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata()) # stored R, G, B data in an array
    
    # Extract the LSB from each pixel's R channel
    # YOUR CODE HERE
    
    # Convert binary message to readable text
    # YOUR CODE HERE
    
    return message


# Run the script 
# DO NOT MODIFY!!!
image_path = './hidden_message.png'
message = extract_lsb(image_path)
print(f"Hidden message: {message}")
