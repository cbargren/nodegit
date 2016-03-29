{
  'targets': [
  {
    "target_name": "zlib",
    "type": "static_library",
    "sources": [
      "libgit2/deps/zlib/adler32.c",
      "libgit2/deps/zlib/crc32.c",
      "libgit2/deps/zlib/crc32.h",
      "libgit2/deps/zlib/deflate.c",
      "libgit2/deps/zlib/deflate.h",
      "libgit2/deps/zlib/inffast.c",
      "libgit2/deps/zlib/inffast.h",
      "libgit2/deps/zlib/inffixed.h",
      "libgit2/deps/zlib/inflate.c",
      "libgit2/deps/zlib/inflate.h",
      "libgit2/deps/zlib/inftrees.c",
      "libgit2/deps/zlib/inftrees.h",
      "libgit2/deps/zlib/trees.c",
      "libgit2/deps/zlib/trees.h",
      "libgit2/deps/zlib/zconf.h",
      "libgit2/deps/zlib/zlib.h",
      "libgit2/deps/zlib/zutil.c",
      "libgit2/deps/zlib/zutil.h",
    ],
    "defines": [
      "NO_VIZ",
      "STDC",
      "NO_GZIP",
    ],
    "conditions": [
      ["OS=='win'", {
        "include_dirs": [
          "libgit2/deps/regex"
        ]
      }]
    ],
    "include_dirs": [
      "libgit2/include"
    ],
    "direct_dependent_settings": {
      "include_dirs": [
        "libgit2/deps/zlib",
      ],
    },
  },
  ],
}
