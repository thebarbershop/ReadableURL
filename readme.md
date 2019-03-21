# readable-url

THIS IS AN INCOMPLETE PROJECT. IT DOESN'T WORK YET.


A Python package and a C++ library to generate readable random phrases to add to dynamically generated URLs like ```https://www.examples.com/WiseAcceptableSnoodPupper```

Forked from [sharadbhat/ReadableURL](https://github.com/sharadbhat/ReadableURL),  an npm package.

## Get started

### Install for Python

```sh
pip install readable-url
```

### Install for C++

Just clone this git repo to your project directory and ```#include "readableurl.h"```.

## Usage Instructions

To use the package, first require it.

```js
const readable = require("readable-url");
```

Then, we create an object.

```js
// Takes 3 parameters.
// 1. A boolean value - If true, returns string in CamelCase, else lowercase.
// 2. An integer value - The number of words to be generated in the string. (Between 2 and 10).
// 3. A string - The seperator between the words.

var generator = new readable(); // true, 3 and '' are the default values.

// var generator = new readable(false, 5, '-'); // Other options.
```

To generate a random phrase,

```js
var url = generator.generate();

console.log(url); // Prints out 'ForgetfulHarshEgg'
```

This can be used to add to the end of a URL.

Example: ```https://example.com/photos/ForgetfulHarshEgg```

For best results, use an integer value of 3, 4, or 5.
