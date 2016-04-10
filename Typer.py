# -*- coding: utf-8 -*- 
import ctypes
from ctypes import wintypes
import time


#TODO: American Or British Keyboard


class MOUSEINPUT(ctypes.Structure):
    # C struct definitions
    wintypes.ULONG_PTR = wintypes.WPARAM
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    # C struct definitions
    wintypes.ULONG_PTR = wintypes.WPARAM
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
#         if not self.dwFlags & KEYEVENTF_UNICODE:
#             self.wScan = user32.MapVirtualKeyExW(self.wVk,
#                                                  MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

class TypeWriter:
    INPUT_MOUSE    = 0
    INPUT_KEYBOARD = 1
    INPUT_HARDWARE = 2
    
    KEYEVENTF_EXTENDEDKEY = 0x0001
    KEYEVENTF_KEYUP       = 0x0002
    KEYEVENTF_UNICODE     = 0x0004
    KEYEVENTF_SCANCODE    = 0x0008
    
    MAPVK_VK_TO_VSC = 0

    # # msdn.microsoft.com/en-us/library/dd375731
    keymap_US = {
        "BACK" : 0x08,
        "TAB" : 0x09,
        "SHIFT" : 0X10,
        "CTRL" : 0x11,
        "ALT" : 0x12,
        "PAUSE" : 0x13,
        "CAPS" : 0x14,
        " " : 0x20,
        "0" : 0x30,
        "1" : 0x31,
        "2" : 0x32,
        "3" : 0x33,
        "4" : 0x34,
        "5" : 0x35,
        "6" : 0x36,
        "7" : 0x37,
        "8" : 0x38,
        "9" : 0x39,
        "a" : 0x41,
        "b" : 0x42,
        "c" : 0x43,
        "d" : 0x44,
        "e" : 0x45,
        "f" : 0x46,
        "g" : 0x47,
        "h" : 0x48,
        "i" : 0x49,
        "j" : 0x4A,
        "k" : 0x4B,
        "l" : 0x4C,
        "m" : 0x4D,
        "n" : 0x4E,
        "o" : 0x4F,
        "p" : 0x50,
        "q" : 0x51,
        "r" : 0x52,
        "s" : 0x53,
        "t" : 0x54,
        "u" : 0x55,
        "v" : 0x56,
        "w" : 0x57,
        "x" : 0x58,
        "y" : 0x59,
        "z" : 0x5A,
        ";" : 0xBA,
        "=" : 0xBB,
        "," : 0xBC,
        "-" : 0xBD,
        "." : 0xBE,
        "/" : 0xBF,
        "`" : 0xC0,
        
        "[" : 0xDB,
        "\\" : 0xDC,
        "]" : 0xDD,
        "'" : 0xDE,
        
        "\n" : 0x0D,
        "ENTER" : 0x0D,
        "LSHIFT" : 0xA0,
        }
    upperlower_US = {
        "~" : "`",
        "!" : "1",
        "@" : "2",
        "#" : "3",
        "$" : "4",
        "%" : "5",
        "^" : "6",
        "&" : "7",
        "*" : "8",
        "(" : "9",
        ")" : "0",
        "_" : "-",
        "+" : "=",
        "{" : "[",
        "}" : "]",
        ":" : ";",
        '"' : "'",
        "|" : "\\",
        "<" : ",",
        ">" : ".",
        "?" : "/",
    }
    keymap_UK = {
        "BACK" : 0x08,
        "TAB" : 0x09,
        "SHIFT" : 0X10,
        "CTRL" : 0x11,
        "ALT" : 0x12,
        "PAUSE" : 0x13,
        "CAPS" : 0x14,
        " " : 0x20,
        "0" : 0x30,
        "1" : 0x31,
        "2" : 0x32,
        "3" : 0x33,
        "4" : 0x34,
        "5" : 0x35,
        "6" : 0x36,
        "7" : 0x37,
        "8" : 0x38,
        "9" : 0x39,
        "a" : 0x41,
        "b" : 0x42,
        "c" : 0x43,
        "d" : 0x44,
        "e" : 0x45,
        "f" : 0x46,
        "g" : 0x47,
        "h" : 0x48,
        "i" : 0x49,
        "j" : 0x4A,
        "k" : 0x4B,
        "l" : 0x4C,
        "m" : 0x4D,
        "n" : 0x4E,
        "o" : 0x4F,
        "p" : 0x50,
        "q" : 0x51,
        "r" : 0x52,
        "s" : 0x53,
        "t" : 0x54,
        "u" : 0x55,
        "v" : 0x56,
        "w" : 0x57,
        "x" : 0x58,
        "y" : 0x59,
        "z" : 0x5A,
        ";" : 0xBA,
        "=" : 0xBB,
        "," : 0xBC,
        "-" : 0xBD,
        "." : 0xBE,
        "/" : 0xBF,
        "`" : 0xC0,
        
        "[" : 0xDB,
        "#" : 0xDC,
        "]" : 0xDD,
        "'" : 0xDE,
        
        "\n" : 0x0D,
        "ENTER" : 0x0D,
        "LSHIFT" : 0xA0,
        }   
        
    upperlower_UK = {
        "??" : "`",
        "!" : "1",
        '"' : "2",
        "¡ê" : "3",
        "$" : "4",
        "%" : "5",
        "^" : "6",
        "&" : "7",
        "*" : "8",
        "(" : "9",
        ")" : "0",
        "_" : "-",
        "+" : "=",
        "{" : "[",
        "}" : "]",
        ":" : ";",
        '@' : "'",
        "~" : "#",           #|" : "\\",
        "<" : ",",
        ">" : ".",
        "?" : "/",
    } 
    
    testString = 'aA1`~!@#$%^&*()_-+=[{]}\|\'";:/?.>,<'
    testLetters = "abcdefghijklmnopqrstuvwxyz"
    
    def __init__(self, layout = "US"):
        if layout == "US":
            self.keymap = self.keymap_US
            self.upperlower = self.upperlower_US
        else:
            self.keymap = self.keymap_UK
            self.upperlower = self.upperlower_UK
            
        self.user32 = ctypes.WinDLL('user32', use_last_error=True)
        LPINPUT = ctypes.POINTER(INPUT)
        self.user32.SendInput.errcheck = self._check_count
        self.user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                                     LPINPUT,       # pInputs
                                     ctypes.c_int)  # cbSize
        
            
        
    ### Special Key Combo ###
    def AltTab(self):
        self.comboKeyIn(self.keymap["ALT"], self.keymap["TAB"], 0.4)

    def CtrlA(self):
        self.comboKeyIn(self.keymap["CTRL"], self.keymap["a"], 0.4)
    ### Helper Funcitons ###
    def keyIn(self, key):
        if key in self.keymap:
            self.singleKeyIn(self.keymap[key])
            # self.comboKeyIn(self.keymap["LSHIFT"], self.keymap[key.upper()])
        elif key.lower() in self.keymap:
            self.comboKeyIn(self.keymap["LSHIFT"], self.keymap[key.lower()])
        elif key in self.upperlower:
            self.comboKeyIn(self.keymap["LSHIFT"], self.keymap[self.upperlower[key]])
            
    def comboKeyIn(self, hexKeyCode1, hexKeyCode2, sleepTime = 0):
        self.pressKey(hexKeyCode1)   
        self.singleKeyIn(hexKeyCode2)
        time.sleep(sleepTime)
        self.releaseKey(hexKeyCode1)
        
    def singleKeyIn(self, hexKeyCode, sleepTime = 0):
        self.pressKey(hexKeyCode)   
        time.sleep(sleepTime)
        self.releaseKey(hexKeyCode)   
        
    def pressKey(self,hexKeyCode):
        x = INPUT(type=TypeWriter.INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode))
        self.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    
    def releaseKey(self, hexKeyCode):
        x = INPUT(type=TypeWriter.INPUT_KEYBOARD,
                  ki=KEYBDINPUT(wVk=hexKeyCode,
                                dwFlags=TypeWriter.KEYEVENTF_KEYUP))
        self.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
        
    def _check_count(self, result, func, args):
        if result == 0:
            raise ctypes.WinError(ctypes.get_last_error())
        return args


if __name__ == "__main__":
    TypeWriter().AltTab()
    
