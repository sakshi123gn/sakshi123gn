import numpy as np

def objective_function(x):
    return np.sum(x**2)

def particle_swarm_optimization(obj_fun, bounds, num_particles=30, max_iter=100, w=0.5, c1=1.5, c2=1.5):
    num_dimensions = len(bounds)
    positions = np.random.rand(num_particles, num_dimensions)
    positions = bounds[:, 0] + positions * (bounds[:, 1] - bounds[:, 0])
    velocities = np.zeros_like(positions)
    personal_best_positions = positions.copy()
    personal_best_values = np.apply_along_axis(obj_fun, 1, personal_best_positions)
    global_best_position = personal_best_positions[np.argmin(personal_best_values)]

    for _ in range(max_iter):
        r1, r2 = np.random.rand(num_particles, num_dimensions), np.random.rand(num_particles, num_dimensions)
        velocities = (w * velocities +
                      c1 * r1 * (personal_best_positions - positions) +
                      c2 * r2 * (global_best_position - positions))
        positions = np.clip(positions + velocities, bounds[:, 0], bounds[:, 1])
        current_values = np.apply_along_axis(obj_fun, 1, positions)
        better_mask = current_values < personal_best_values
        personal_best_positions[better_mask] = positions[better_mask]
        personal_best_values[better_mask] = current_values[better_mask]
        global_best_position = personal_best_positions[np.argmin(personal_best_values)]

    return global_best_position, obj_fun(global_best_position)

bounds = np.array([[-10, 10], [-10, 10]])
best_position, best_value = particle_swarm_optimization(objective_function, bounds)
print("Best position found:", best_position)
print("Best value found:", best_value)
