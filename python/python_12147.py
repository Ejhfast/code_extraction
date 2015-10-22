# matplotlib arrows between 3 points
def drawArrow(A, B):
    plt.arrow(A[0], A[1], B[0] - A[0], B[1] - A[1],
              head_width=3, length_includes_head=True)
