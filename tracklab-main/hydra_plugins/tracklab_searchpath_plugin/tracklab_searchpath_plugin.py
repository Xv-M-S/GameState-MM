from hydra.core.config_search_path import ConfigSearchPath
from hydra.plugins.search_path_plugin import SearchPathPlugin
from importlib.metadata import entry_points
import logging

log = logging.getLogger(__name__)


class PbTrackSearchPathPlugin(SearchPathPlugin):
    def manipulate_search_path(self, search_path: ConfigSearchPath) -> None:
        # Appends the search path for tracklab plugins to the end of the search path
        # 修改：手动添加
        search_path.append(provider="sn-gamestate", path="file://./sn_gamestate/configs")
        search_path.append(provider="tracklab", path="pkg://plugins.track.bot_sort")
        search_path.append(provider="tracklab", path="pkg://plugins.track.bpbreid_strong_sort")
        search_path.append(provider="tracklab", path="pkg://plugins.track.byte_track")
        search_path.append(provider="tracklab", path="pkg://plugins.track.deep_oc_sort")
        search_path.append(provider="tracklab", path="pkg://plugins.track.oc_sort")
        search_path.append(provider="tracklab", path="pkg://plugins.track.strong_sort")