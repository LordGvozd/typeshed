import sys
from _typeshed import FileDescriptor
from typing import NamedTuple

from gevent._ffi.loop import AbstractLoop
from gevent._types import _IoWatcher
from gevent.libuv import watcher

def get_version() -> str: ...
def get_header_version() -> str: ...
def supported_backends() -> list[str]: ...

class loop(AbstractLoop):
    CALLBACK_CHECK_COUNT: int
    SIGNAL_CHECK_INTERVAL_MS: int
    approx_timer_resolution: float
    error_handler: None
    def __init__(self, flags: int | None = None, default: bool | None = None) -> None: ...

    class _HandleState(NamedTuple):
        handle: int
        type: str
        watcher: watcher.watcher
        ref: bool
        active: bool
        closing: bool

    def debug(self) -> list[_HandleState]: ...
    def install_sigchld(self) -> None: ...
    def reset_sigchld(self) -> None: ...
    # this returns a class private to gevent.libuv.watcher.io, which satisifies the protocol
    def io(self, fd: FileDescriptor, events: int, ref: bool = True, priority: int | None = None) -> _IoWatcher: ...
    def closing_fd(self, fd: FileDescriptor) -> bool: ...
    def timer(self, after: float, repeat: float = 0.0, ref: bool = True, priority: int | None = None) -> watcher.timer: ...
    def signal(self, signum: int, ref: bool = True, priority: int | None = None) -> watcher.signal: ...
    def idle(self, ref: bool = True, priority: int | None = None) -> watcher.idle: ...
    def check(self, ref: bool = True, priority: int | None = None) -> watcher.check: ...
    def async_(self, ref: bool = True, priority: int | None = None) -> watcher.async_: ...
    if sys.platform != "win32":
        def fork(self, ref: bool = True, priority: int | None = None) -> watcher.fork: ...
        def child(self, pid: int, trace: int = 0, ref: bool = True) -> watcher.child: ...
    # prepare is not supported on libuv yet, but we need type_error to annotate that

__all__: list[str] = []
