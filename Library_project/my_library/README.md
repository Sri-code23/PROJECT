QuotesEngine Library User Guide
==========================

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Examples](#examples)
5. [Troubleshooting](#troubleshooting)

Introduction
------------

QuotesEngine is a Python library designed to display random motivational quotes. The library is easy to use and provides a simple way to add motivation to your applications for some fun and creatives. this is just my first project so I am open to any feedback or suggestions. I am excited to share this with you and I hope you enjoy using it. 
```bash
Important Note ! 

#This is a test library created solely for educational purposes, to learn and understand the process of developing a Python library. Please note that this library is not intended for any serious applications, but rather for personal learning and experimentation. Your feedback and suggestions are highly appreciated, and will help me improve my skills and knowledge in creating Python libraries
```

# Installation
------------

To install the QuotesEngine library, run the following command in your terminal:

```bash
#to installl the library
pip install QuotesEngine
```

Usage
-----

To use the QuotesEngine library, simply import the `QuotesEngine` class and create an instance of it. You can then call the `Motivate` method to display a random motivational quote.

```python
#to initialise
import QuotesEngine

object_name= QuotesEngine.Motivate.username("Your name")
object_name.motivate()
```

Examples
--------

Here are a few examples of how you can use the QuotesEngine library:

### Display a Random Motivational Quote

```python
#example 
import QuotesEngine

person1=QuotesEngine.Motivate.username("sol")
person1.motivate()

```
### output :

```python
#output

Hello dhj !,  this is my first package 
┌────────────────────────────────────────────────────────────────┐
│     Little things make big days, dhj. Cherish every moment.    │
└────────────────────────────────────────────────────────────────┘
```

Troubleshooting
---------------

If you encounter any issues while using the Motivate library, please check the following:

* Make sure you have installed the library correctly.

    ```bash
    pip install QuotesEngine
    ```
* Check that you are using the correct syntax to import and use the library.
* If you are still having issues, I apologize if it's due to any oversight on my part during development. Please don't hesitate to reach out and provide your feedback, as it will help me improve the library and better serve you in the future.

Library Information
------------------

* Author: Sridharan
* Version: [2.0]()
* Country: India
* License: MIT [LICENSE](LICENSE)
* contact: sridharansri2312@gmail.com


