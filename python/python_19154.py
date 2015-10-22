# How to declare generic type function in scala?
def divide[T](lst:Seq[T], pairs:Seq[(Int, Int)]):Seq[Seq[T]] = {
    pairs.map{case (b, u) =&gt; lst.slice(b,u)}
}
