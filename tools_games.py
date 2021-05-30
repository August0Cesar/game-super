def follow_direction(owner, direction):
        if direction.length != 0:
            owner.alignAxisToVect(direction, 1, 0.8)
            owner.alignAxisToVect([0, 0, 1], 2, 1)