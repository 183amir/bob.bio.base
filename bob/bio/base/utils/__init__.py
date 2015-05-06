#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Laurent El Shafey <Laurent.El-Shafey@idiap.ch>
# Roy Wallace <roy.wallace@idiap.ch>

from .resources import *
from .io import *
from .singleton import *

import numpy

def score_fusion_strategy(strategy_name = 'avarage'):
  """Returns a function to compute a fusion strategy between different scores.

  Different strategies are employed:

  * ``'average'`` : The averaged score is computed using the :py:func:`numpy.average` function.
  * ``'min'`` : The minimum score is computed using the :py:func:`min` function.
  * ``'max'`` : The maximum score is computed using the :py:func:`max` function.
  * ``'median'`` : The median score is computed using the :py:func:`numpy.median` function.
  * ``None`` is also accepted, in which case ``None`` is returned.
  """
  try:
    return {
        'average' : numpy.average,
        'min' : min,
        'max' : max,
        'median' : numpy.median,
        None : None
    }[strategy_name]
  except KeyError:
#    warn("score fusion strategy '%s' is unknown" % strategy_name)
    return None


def selected_indices(total_number_of_indices, desired_number_of_indices = None):
  """Returns a list of indices that will contain exactly the number of desired indices (or the number of total items in the list, if this is smaller).
  These indices are selected such that they are evenly spread over the whole sequence."""
  if desired_number_of_indices is None or desired_number_of_indices >= total_number_of_indices or desired_number_of_indices < 0:
    return range(total_number_of_indices)
  increase = float(total_number_of_indices)/float(desired_number_of_indices)
  # generate a regular quasi-random index list
  return [int((i +.5)*increase) for i in range(desired_number_of_indices)]


def selected_elements(list_of_elements, desired_number_of_elements = None):
  """Returns a list of elements that are sub-selected from the given list (or the list itself, if its length is smaller).
  These elements are selected such that they are evenly spread over the whole list."""
  total_number_of_elements = len(list_of_elements)
  if desired_number_of_elements is None or desired_number_of_elements >= total_number_of_elements or desired_number_of_elements < 0:
    return list_of_elements
  # sub-select
  return [list_of_elements[i] for i in selected_indices(total_number_of_elements, desired_number_of_elements)]
