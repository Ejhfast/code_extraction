# board_list = Board.objects.annotate(num_posts=Count('post')).order_by('num_posts')
