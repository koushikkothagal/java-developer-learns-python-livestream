TODO:
- dunder methods
- how odoes paths work when using symlinks?
- Ordering of paths when importing modules. What comes first? How would some one override teh system modules.  This worked for random but not for sys. What's the difference?
- What is this? Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.
- Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing __dict__ directly. (https://docs.python.org/3/tutorial/classes.html)
- Instance method objects have attributes, too: m.__self__ is the instance object with the method m(), and m.__func__ is the function object corresponding to the method.



