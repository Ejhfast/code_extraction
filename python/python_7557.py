# How to pass a function and its arguments through a wrapper function in R? Similar to *args and *kwargs in python
wrapper &lt;- function(func, ...) {
    func(...)
}
