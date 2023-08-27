def is_clicked_inside_area(point, vertices):
    # Check if a point is inside a polygon defined by its vertices
    x, y = point
    num_vertices = len(vertices)
    j = num_vertices - 1
    odd_nodes = False

    for i in range(num_vertices):
        xi, yi = vertices[i]
        xj, yj = vertices[j]

        if yi < y <= yj or yj < y <= yi:
            if xi + (y - yi) / (yj - yi) * (xj - xi) < x:
                odd_nodes = not odd_nodes

        j = i

    return odd_nodes
