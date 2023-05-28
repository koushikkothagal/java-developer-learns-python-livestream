TODO:
- dunder methods
- how odoes paths work when using symlinks?
- Ordering of paths when importing modules. What comes first? How would some one override teh system modules.  This worked for random but not for sys. What's the difference?
- What is this? Python does not check the cache in two circumstances. First, it always recompiles and does not store the result for the module that’s loaded directly from the command line. Second, it does not check the cache if there is no source module. To support a non-source (compiled only) distribution, the compiled module must be in the source directory, and there must not be a source module.

