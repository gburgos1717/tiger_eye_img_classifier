# Tiger Eye Gemstone Image Classification
_____________________________________________________
# Overview

Tiger eye is a respected gemstone with many variations of color. The most popular of tiger eyes is gold, followed by blue and red. I wanted to develop an image classifier which will determine the type of tiger eye gemstone based on its color. From a business perspective, an accurate gemstone image classifier can help stakeholders engage with natural stones and develop interest to buy or sell. 

The tiger eye image classifier will determine if the stone present in the photo is either a red tiger eye, blue tiger eye, or gold tiger eye. A neural network model will train image data and predict the variations of color under multi-classification.

_________________________________________________________
# Problem Statement

### How can we contribute our gemstone stakeholders and products? 
### What will we have to do to expand and increase sales to a growing market?

I decided to tackle this challenge by generating a prototype gemstone app focused on Tiger Eye.
I think the app can generate the following results when completed:
- Increase Sales
- Increase return of business especially from new gemstone stakeholders
- Provide knowledge from a user friendly app and stakeholders new to the gemstone market
- With a successful interactive app it will be sufficient to target younger demographics such as high school students, ages 14-18 and young adults age 19-25
________________________________________________________

# Selenium Notes for Data Collection

Selenium is used to scrape google images and screenshot images under tiger eye search results. In order to use Selenium "pip install selenium" and download a driver. Examples of drivers for compatible operating systems can be found using the Selenium documentation link provided [link](https://selenium-python.readthedocs.io/installation.html).

Driver note: No matter which driver you decided to use. Just ensure to always provide the correct path to the driver's location. For example here is how a driver location will look for Chrome:

**webdriver.Chrome(r"C:\Users\gburg\Desktop\Scrape\chromedriver.exe")**

All other things Selenium can be researched online as you would learning any other package. Feel free to reference the "img_download_code.ipynb" code to see how Selenium executes a scrape. Just remember to update the driver path location to your local machine set up.

# Data

The image download notebook file uses Selenium to scrape images from Google. Thousands of images were scraped to a local folder where cleaning will take place. Since Selenium is using a screenshot function to bring in images into the image folder photo cleaning is needed. Delete what is irrelevant to the search and images poorly cropped.

The function created in the image download file will allow developers to bring in images to the appropriate label folder. Reference the function documentation for a straight forward explanation.

By each folder generated from the image download file will be a class for the image data.

# Model

A deep learning neural network model was generated to create predictions on each tiger eye color class: Red, Blue, or Gold.
Four conventional layers were constructed each followed by batch normalization. Every two layers(2nd and 4th) was followed by max pooling and a dropout layer of 50%. 

The second to last layer was densed to 64 neurons. Followed by the output layer, densed to 3 neurons, equivalent to the number of color classes with an activation function of softmax.

## Compile

The CNN model was compiled at a batch size of 128 and 20 epochs. An early stop was instantiated for the callback parameter. For example, the original model ran at 13 epochs provided by early stop. Results can be subjective based on the amount of image data collected as well as the parameters provided within batch size and epochs. 

The model compiled to metrics set to accuracy, the optimizer set to adam, and a categorical cross entropy loss function.

# Recommendations

The model is focused on generating different colors to the tiger eye gemstone. Depending on the amount of data generated the data can range from small to large as well as unbalanced to balanced. This will affect the curve of the both loss and accuracy scores. If a small dataset will be used, I recommend trying data augmentation with the image data generator by keras. Reference the following link to indulge in ways to work with small image data. [LINK](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)

# Next Steps

Based on the model I've generated I would like to update my model to a multi-label classification to help identify mixed tiger eye stones. I would like to generate a model that can predict the amount of red and brown colors present on the stone in each image. 

I would also like to incorporate text data to further evaluate what stakeholders have to say about gemstones and text that describes healing properties of each tiger eye stone. 

Eventually I would like to add on other types of stones and each subtype each stone has similar to tiger eye.

# Outcome

The model provided can help generate a solid classifier given the code runs a very stable streamlit prototype application. If updated further the gemstone classifier can be used for all stones alike. Tiger eye is a great start due to its complexity of colors. If successful, whole and retail online stores can benefit from the application by gaining exposure to their gemstone inventory; and provide customers better knowledge and expectations. The younger generation is very interactive to applications especially if the user interface is streamlined to master simplicity. This model can help generate a successful gemstone classifying application.