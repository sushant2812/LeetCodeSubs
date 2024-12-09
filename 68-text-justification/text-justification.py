class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Initialize the result list, current line, and the width of the current line
        res, line, width = [], [], 0

        # Iterate through each word
        for w in words:
            # Check if adding the word would exceed the maximum width
            if width + len(w) + len(line) > maxWidth:
                # Distribute spaces to justify the current line
                # (maxWidth - width) determines how many spaces need to be added
                # Distribute spaces cyclically between words
                for i in range(maxWidth - width):
                    # Add space to each word in round-robin fashion
                    line[i % (len(line) - 1 or 1)] += ' '
                # Add the justified line to the result
                res.append(''.join(line))
                # Reset the current line and width for the next line
                line, width = [], 0
            
            # Add the current word to the line
            line.append(w)
            # Update the width of the current line (only counts characters in words, not spaces)
            width += len(w)

        # Handle the last line (left-justify)
        # Join words with a single space and pad with spaces to reach maxWidth
        res.append(' '.join(line).ljust(maxWidth))
        
        # Return the fully justified text as a list of lines
        return res