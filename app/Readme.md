# WorqHat Python Library

The worqhat package is a comprehensive library that allows developers to interact with the WorqHat API. It provides a simple and intuitive interface to access various AI services such as content generation, image generation,text extraction,image analysis and much more. It includes ready-made functions for both AI models and the Database.

This library provides convenient access to the WorqHat APIs from Python.

To learn how to use the WorqHat APIs,check out our [API Reference](https://docs.worqhat.com/api-reference/authentication)
and [Documentation](https://docs.worqhat.com/introduction)

## Table of Contents

- [Worqhat Python Library](#worqhat-python-library)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Importing Worqhat library](#importing-worqhat-library)
    - [Initializing Worqhat library](#initializing-worqhat-library)
    - [Verifying User Profile](#verifying-user-profile)
    - [Sample Functions](#sample-functions)
      - [Content Moderation with AiCon V2](#content-moderation-with-aicon-v2)
      - [Image Analysis with AiCon V2](#image-analysis-with-aicon-v2)
  - [Documentation](#documentation)
  - [License](#license)
  - [Contributing](#contributing)
  - [Support](#support)

## Installation

You can install the Worqhat Python Library via pip:

```bash
pip install worqhat
```

## Usage

### Importing Worqhat Libary

```python
import worqhat
```

### Initializing Worqhat Library

To use the WorqHat library you need to create a .env file which will look like

```
API_KEY="Your API-KEY"
```

You will also need to install and import python-dotenv library and use a load_dotenv object

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv

load_dotenv()
```

You can also pass the API_KEY as a parameter to the functions of the library.

### Sample Functions

#### Content Moderation with AiCon V2

```python
from worqhat.ai_models import content_mod
from dotenv import load_dotenv
load_dotenv()
images=["orange.png"]
r=content_mod.content_moderation("Hi! How are you")
print(r)

```

#### Image Analysis with AiCon V2

```python
from worqhat import analyze_images
from dotenv import load_dotenv
load_dotenv()
images=["path-to-image-1","path-to-image-2"]
r=analyze_images(images,"What is this")
print(r)
```

## Documentation

For detailed documentation, please visit our [official documentation](https://docs.worqhat.com).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions from the community. Please read our contributing guidelines for more information.

## Support

If you encounter any issues or have any questions, please file an issue on our [GitHub issues page](https://github.com/Ayush-Kul/worqhat-python/issues).

```

This README provides installation instructions, usage examples, links to documentation and license information, as well as details on how to contribute and seek support. Adjust the placeholders (such as `"your-api-key"`, etc.) with your actual values and add more content or sections as needed.
```
