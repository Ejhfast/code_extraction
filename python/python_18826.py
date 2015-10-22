# python loop and print string with variables
for i in range(5):
    print  ("&lt;li&gt; %d. &lt;a href='/some/url/index.php?member=_MEMBER_%d_'&gt;_MEMBER_1_DESC_ (_MEMBER_%d_UNI_IN_) &lt;/a&gt;&lt;/li&gt;") % **(i, i, i)**
