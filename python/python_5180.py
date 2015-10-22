# KeyboardHookProc in DLL doesn't do anything when called from python
hKeyboardHook = SetWindowsHookEx(WH_KEYBOARD, KeyboardProc, NULL, 0);
