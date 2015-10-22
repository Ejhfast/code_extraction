# List of installed fonts OS X / C
import Cocoa
manager = Cocoa.NSFontManager.sharedFontManager()
font_families = list(manager.availableFontFamilies())
