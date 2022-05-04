scene.set_background_image(assets.image("""
    myImage
"""))
lion = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.player)
lion.set_position(10, 90)
scaling.scale_by_pixels(lion, 15, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
rabbit = sprites.create(assets.image("""
    myImage1
"""), SpriteKind.player)
rabbit.set_position(31, 90)
scaling.scale_by_pixels(rabbit, 7, ScaleDirection.UNIFORMLY, ScaleAnchor.MIDDLE)
goat = sprites.create(assets.image("""
    myImage3
"""), SpriteKind.player)
goat.set_position(46, 90)
owl = sprites.create(assets.image("""
    myImage6
"""), SpriteKind.player)