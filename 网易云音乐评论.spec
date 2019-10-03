# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\ÎÒÊÇÙ¡Àöæ«\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\PyInstaller\\ÍøÒ×ÔÆÒôÀÖÅÀ³æ\\ÍøÒ×ÔÆÒôÀÖÆÀÂÛ.py'],
             pathex=['C:\\Users\\ÎÒÊÇÙ¡Àöæ«\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\PyInstaller\\ÍøÒ×ÔÆÒôÀÖÅÀ³æ'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ÍøÒ×ÔÆÒôÀÖÆÀÂÛ',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ÍøÒ×ÔÆÒôÀÖÆÀÂÛ')
