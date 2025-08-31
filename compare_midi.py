
from music21 import converter
import sys

def compare_files(file1, file2):
    """Compares two MIDI files and prints the differences."""
    try:
        midi_1 = converter.parse(file1)
        midi_2 = converter.parse(file2)

        notes_1 = [str(element.pitch) if hasattr(element, 'pitch') else '.'.join(str(n) for n in element.normalOrder) for element in midi_1.flat.notes]
        notes_2 = [str(element.pitch) if hasattr(element, 'pitch') else '.'.join(str(n) for n in element.normalOrder) for element in midi_2.flat.notes]

        print(f"--- Comparing {file1} and {file2} ---")
        differences_found = 0
        for i in range(min(len(notes_1), len(notes_2))):
            if notes_1[i] != notes_2[i]:
                differences_found += 1
                print(f"Difference at note #{i+1}:")
                print(f"  - {file1}: {notes_1[i]}")
                print(f"  - {file2}: {notes_2[i]}")
                print("-" * 20)

        if differences_found == 0:
            print("No differences found.")
        else:
            print(f"Found a total of {differences_found} differing notes.")

    except FileNotFoundError as e:
        print(f"Error: Could not find a file. Please check filenames. Details: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage: Takes filenames from command line arguments
    # python compare_midi.py file1.mid file2.mid
    if len(sys.argv) != 3:
        print("Usage: python compare_midi.py <file1.mid> <file2.mid>")
    else:
        compare_files(sys.argv[1], sys.argv[2])
