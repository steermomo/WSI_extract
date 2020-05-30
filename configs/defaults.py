from yacs.yacs_config import CfgNode as CN
import os.path as osp
# https://github.com/rbgirshick/yacs

_C = CN()

_C.DEST_EXT = "png"
_C.SAVE_PATCH = False


_C.SLIDE = CN()

_C.SLIDE.BASE_DIR = ''
_C.SLIDE.SCALE_FACTOR = 32
_C.SLIDE.DEST_DIR = ''
_C.SLIDE.THUMBNAIL_SIZE = 300
_C.SLIDE.THUMBNAIL_EXT = "jpg"
_C.SLIDE.PREFIX = ''
_C.SLIDE.SRC_DIR = ""
_C.SLIDE.SRC_EXT = "SVS"
_C.SLIDE.DEST_SUFFIX = ""
_C.SLIDE.DEST_EXT = 'jpg'
_C.SLIDE.DEST_THUMBNAIL_DIR = osp.join(_C.SLIDE.BASE_DIR, 'thumbnail_' + _C.SLIDE.THUMBNAIL_EXT)


_C.FILTER = CN()
_C.FILTER.SUFFIX = ""
_C.FILTER.RESULT_TEXT = "filtered"
_C.FILTER.DIR = osp.join(_C.SLIDE.BASE_DIR, "filter_thumbnail_" + _C.SLIDE.THUMBNAIL_EXT)
_C.FILTER.PREFIX = ""
_C.FILTER.THUMBNAIL_DIR = ""


_C.TILE.SUMMARY_DIR = osp.join(_C.SLIDE.BASE_DIR, "tile_summary_" + _C.DEST_EXT)
_C.TILE.SUMMARY_ON_ORIGINAL_DIR = osp.join(_C.SLIDE.BASE_DIR, "tile_summary_on_original_" + _C.DEST_EXT)
_C.TILE.SUMMARY_SUFFIX = "tile_summary"
_C.TILE.SUMMARY_THUMBNAIL_DIR = osp.join(_C.SLIDE.BASE_DIR, "tile_summary_thumbnail_" + _C.DEST_EXT)
_C.TILE.SUMMARY_ON_ORIGINAL_THUMBNAIL_DIR = osp.join(_C.SLIDE.BASE_DIR, "tile_summary_on_original_thumbnail_" + _C.SLIDE.THUMBNAIL_EXT)
_C.TILE.SUMMARY_PAGINATION_SIZE = 50
_C.TILE.SUMMARY_PAGINATE = True
_C.TILE.SUMMARY_HTML_DIR = _C.SLIDE.BASE_DIR

_C.TILE.PATCH_IDX = ""

_C.TILE.DATA_DIR = osp.join(_C.SLIDE.BASE_DIR, "tile_data")
_C.TILE.DATA_SUFFIX = "tile_data"
_C.TOP_TILES_SUFFIX = "top_tile_summary"
_C.TOP_TILES_DIR = osp.join(_C.SLIDE.BASE_DIR, _C.TOP_TILES_SUFFIX + "_" + _C.DEST_EXT)
_C.TOP_TILES_THUMBNAIL_DIR = osp.join(_C.SLIDE.BASE_DIR, _C.TOP_TILES_SUFFIX + "_thumbnail_" + _C.DEST_EXT)
_C.TOP_TILES_ON_ORIGINAL_DIR = osp.join(_C.SLIDE.BASE_DIR, _C.TOP_TILES_SUFFIX + "_on_original_" + _C.DEST_EXT)
# _C.TOP_TILES_ON_ORIGINAL_THUMBNAIL_DIR = osp.join(_C.SLIDE.BASE_DIR,

_C.TILE_DIR = osp.join(_C.SLIDE.BASE_DIR, "tiles_" + _C.DEST_EXT)
_C.TILE_SUFFIX = "tile"

STATS_DIR = osp.join(_C.SLIDE.BASE_DIR, "svs_stats")


def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  # Return a clone so that the defaults will not be altered
  # This is for the "local variable" use pattern
  return _C.clone()