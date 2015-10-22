# bottle python rendering variable as text and not html
%for postlist in postlist:
    &lt;li&gt; {{ !postlist }}
%end
