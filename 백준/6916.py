import sys

sys.stdin = open("6916.txt", "r")

ls = [
    """ * * *
*     *
*     *
*     *

*     *
*     *
*     *
 * * *""",
    """
      *
      *
      *

      *
      *
      *
""",
    """ * * *
      *
      *
      *
 * * *
*
*
*
 * * * """,
    """ * * *
      *
      *
      *
 * * *
      *
      *
      *
 * * *""",
    """
*     *
*     *
*     *
 * * *
      *
      *
      *
""",
    """ * * *
*
*
*
 * * *
      *
      *
      *
 * * *""",
    """ * * *
*
*
*
 * * *
*     *
*     *
*     *
 * * *""",
    """ * * *
      *
      *
      *

      *
      *
      *
""",
    """ * * *
*     *
*     *
*     *
 * * *
*     *
*     *
*     *
 * * *""",
    """ * * *
*     *
*     *
*     *
 * * *
      *
      *
      *
 * * *""",
]


a=int(input())

print(ls[a])