# How to specify a custom 404 view for Django using Class Based Views?
from path.to.view import Custom404
handler404 = Custom404.as_view()
