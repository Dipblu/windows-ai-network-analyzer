from app.capture.engine import CaptureEngine


def test_capture_engine_initial_state() -> None:
    """
    Verify that a new CaptureEngine starts in the Idle state.
    """
    engine = CaptureEngine()

    assert engine.is_capturing() is False


def test_start_capture() -> None:
    """
    Verify that start_capture() changes the state to Capturing.
    """
    engine = CaptureEngine()

    engine.start_capture()

    assert engine.is_capturing() is True


def test_stop_capture() -> None:
    """
    Verify that stop_capture() changes the state back to Idle.
    """
    engine = CaptureEngine()

    engine.start_capture()
    engine.stop_capture()

    assert engine.is_capturing() is False