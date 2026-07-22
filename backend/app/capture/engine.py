"""
Capture Engine

Responsible for managing packet capture operations.

Current Status:
- Architecture only
- Packet capture will be implemented in later tasks
"""


class CaptureEngine:
    """
    Coordinates packet capture operations.

    This class will eventually:
    - Discover network interfaces
    - Start packet capture
    - Stop packet capture
    - Report capture status
    - Stream packets to other components

    It does NOT:
    - Decode packets
    - Display packets
    - Analyze packets
    - Save packets
    """

    def __init__(self) -> None:
        """Initialize the capture engine."""
        self._is_capturing: bool = False

    def is_capturing(self) -> bool:
        """
        Return the current capture state.
        """
        return self._is_capturing
    
    def start_capture(self) -> None:
        """
        Start a packet capture session.

        This method currently changes the internal capture state.
        Future versions will initialize the actual packet capture engine.
        """
        self._is_capturing = True

    def stop_capture(self) -> None:
        """
        Stop the current packet capture session.

        This method currently changes the internal capture state.
        Future versions will safely shut down the packet capture engine
        and release any allocated resources.
        """
        self._is_capturing = False

    