#!/usr/bin/env python2

# Copyright (c) 2012 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

f = open(sys.argv[1], 'w+')
f.write('Hello from touch.py\n')
f.close()
