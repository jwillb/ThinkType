# ThinkType

ThinkType is a ridiculously simple Python script that allows control of the LED light on the back of most (I think) ThinkPad laptops running Linux.

## Prerequisites
You will need:
- A ThinkPad running Linux
- To add two new lines to ```/etc/modules```. These lines are:  
```ec_sys```  
```ec_sys write_support=1```  
 You may also do something like ```sudo modprobe -r ec_sys ec_sys write_support=1```. However, modprobe is temporary, and will reset on the next boot.
 
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

### Current Issues:
- After a while, the script seems to stop functioning. This may be isolated to my machine, but it seems like the python script is shut down after a while causing the LED to be permanently shut off, unless you directly write to the ```io``` file in ```/sys/debug/ec/ec0/```.
