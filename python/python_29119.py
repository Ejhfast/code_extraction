# Deleting Entities in NDB last child is always being deleted
document.body.innerHTML += '&lt;form id="dynForm" action="/delete" method="post"&gt;&lt;input type="hidden" name="for_deletion" value=' + urlsafe + '&gt;&lt;/form&gt;';
         document.getElementById("dynForm").submit();
