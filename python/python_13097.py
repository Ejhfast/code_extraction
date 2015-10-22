# How to make field in OpenERP required only for specific workflow state?
&lt;field name="fiscal_position" attrs="{'required':[('state','in',['pending','open'])]}"/&gt;
