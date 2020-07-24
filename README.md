# ThinkType

ThinkType is a riciduclously simple Python script that allows control of the LED light on the back of most ThinkPad laptops running Linux.

## Prerequisites
You will need:
- A ThinkPad running Linux
- To add two new lines to ```/etc/modules```. These lines are:
```ec_sys```
```ec_sys write_support=1```
 You may also use ```modprobe```. However, modprobe is temporary, and will reset on the next boot.
 
### The following keys will activate the LED, when either pressed once or held down:
- ```Enter```
- ```Shift```
- ```Alt```
- ```Tab```
- ```Delete```
- ```Backspace```
- ```Escape```
- ```Space```  
More may come in the future.
