# Python float to string: how to get '0.03' but '-.03'
s = ('%4.2f' % n).replace('-0','-')
