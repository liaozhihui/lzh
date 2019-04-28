# coding=utf-8
import re
content="""
<div class="animal">
    <p class="name">
        <a tilte="Tiger"></a>
    </p>
    <p class="content">
        Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
        <a tilte="Rabbit"></a>
    </p>
    <p class="content">
        Small white rabbit white and white
    </p>
</div>
"""
p=re.compile('<div class="animal">.*?<a tilte="(.*?)".*?content">(.*?)</p>.*?</div>',re.S)
p_list=p.findall(content)
print(p_list)