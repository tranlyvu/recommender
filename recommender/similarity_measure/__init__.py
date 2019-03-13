"""
	Recommender
	-----
	recommender is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""

from .cosine import cosine
from .euclidean import euclidean_distance
from .pearson import pearson_correlation

__all__=['cosine',
		 'euclidean_distance',
		 'pearson_correlation'
		]

__version__ = '1.1.0'
__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__license__ = "Apache License 2.0"
