x = sp.symbols()
sync = sp.Placewise(
  ( 1, x == 0 ),
  ( sp.sin(x)/x, True )
)

display( sp.Eq( sp.Function("sync")(x), sync ) )