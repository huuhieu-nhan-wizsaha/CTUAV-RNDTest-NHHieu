import os

# Mapping class name to class_id
CLASS_MAP = {
    'plane': 1,
    'ship': 2,
    'large-vehicle': 3,
    'small-vehicle': 4,
}

def obb_to_aabb(coords):
    xs = coords[0::2]
    ys = coords[1::2]
    x_min, x_max = int(min(xs)), int(max(xs))
    y_min, y_max = int(min(ys)), int(max(ys))
    return [x_min, y_min, x_max, y_max]

def convert_dota_format(input_dir, output_dir, selected_classes=None):
    os.makedirs(output_dir, exist_ok=True)
    ann_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

    for ann_file in ann_files:
        input_path = os.path.join(input_dir, ann_file)
        output_path = os.path.join(output_dir, ann_file)

        with open(input_path, 'r') as fin:
            lines = fin.readlines()

        # Skip 2 first lines (metadata)
        object_lines = lines[2:]

        with open(output_path, 'w') as fout:
            for line in object_lines:
                parts = line.strip().split()
                if len(parts) < 10:
                    continue  # skip invalid line

                coords = list(map(float, parts[:8]))
                category = parts[8].strip()
                difficult = int(parts[9])

                if selected_classes and category not in selected_classes:
                    continue  # skip unselected classes

                if category not in CLASS_MAP:
                    continue  # skip the unmapped classes

                bbox = obb_to_aabb(coords)
                class_id = CLASS_MAP[category]
                fout.write(f"{bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {class_id}\n")

    print(f"{len(ann_files)} annotation file has been converted to AABB format..")

def main():
    input_train_dir = "../dataset/train/annotations"
    convert_dota_format(input_train_dir, input_train_dir)

    input_test_dir = "../dataset/test/annotations"
    convert_dota_format(input_test_dir, input_test_dir)

if __name__ == "__main__":
	main()
