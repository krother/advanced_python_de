"""
MagicMock: an object that fits to everything
"""
from unittest.mock import MagicMock

mm = MagicMock()

# these just work and return more MagicMocks
mm.plot
mm.get_icecream()
mm.select(id=1234, elephant=True).filter(foo="bar").limit(10)


# non-magic attributes for testing whether the mock has been used
mm.select.called

mm.select.call_count
mm.select(dummy=3)
mm.select.call_count

