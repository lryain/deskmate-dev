# Copyright (c) 2014 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'hello',
      'type': 'executable',
      'sources': [
        'hello.c',
      ],
      'aosp_build_settings': {
        'LOCAL_MODULE_SUFFIX': ['.foo'],
      }
    },
  ],
}
