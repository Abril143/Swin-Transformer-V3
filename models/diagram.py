import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_swin_transformer_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Draw the boxes
    ax.add_patch(patches.FancyBboxPatch((0.05, 0.8), 0.1, 0.1, boxstyle="round,pad=0.02", edgecolor="black", facecolor="white"))
    ax.text(0.1, 0.85, "Images", ha="center", va="center")
    
    ax.add_patch(patches.FancyBboxPatch((0.2, 0.8), 0.15, 0.1, boxstyle="round,pad=0.02", edgecolor="black", facecolor="white"))
    ax.text(0.275, 0.85, "Patch Partition", ha="center", va="center")
    
    ax.add_patch(patches.FancyBboxPatch((0.4, 0.8), 0.15, 0.1, boxstyle="round,pad=0.02", edgecolor="black", facecolor="white"))
    ax.text(0.475, 0.85, "Linear Embedding", ha="center", va="center")
    
    stages = ["Stage 1", "Stage 2", "Stage 3", "Stage 4"]
    x_coords = [0.6, 0.75, 0.9, 1.05]
    for i, (stage, x) in enumerate(zip(stages, x_coords)):
        height = 0.1 * (i + 1)
        ax.add_patch(patches.FancyBboxPatch((x, 0.8 - height/2), 0.15, height, boxstyle="round,pad=0.02", edgecolor="black", facecolor="white"))
        ax.text(x + 0.075, 0.8, stage, ha="center", va="center")
        ax.text(x + 0.075, 0.75, "Swin Transformer Block", ha="center", va="center")
    
    # Draw arrows
    ax.arrow(0.15, 0.85, 0.05, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    ax.arrow(0.35, 0.85, 0.05, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    ax.arrow(0.55, 0.85, 0.05, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    for x in x_coords[:-1]:
        ax.arrow(x + 0.15, 0.85, 0.05, 0, head_width=0.03, head_length=0.02, fc='black', ec='black')
    
    plt.axis('off')
    plt.show()

draw_swin_transformer_diagram()
