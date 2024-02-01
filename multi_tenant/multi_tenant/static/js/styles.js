function brightenColor(hex, percent) {
    // Convert hex to RGB
    hex = hex.replace(/^#/, '');
    const bigint = parseInt(hex, 16);
    const r = (bigint >> 16) & 255;
    const g = (bigint >> 8) & 255;
    const b = bigint & 255;

    // Calculate brightness adjustment
    const adjust = percent / 100;

    // Adjust RGB values
    const adjustedR = Math.min(255, r + (255 - r) * adjust);
    const adjustedG = Math.min(255, g + (255 - g) * adjust);
    const adjustedB = Math.min(255, b + (255 - b) * adjust);

    // Convert back to hex
    const result = ((1 << 24) + (Math.round(adjustedR) << 16) + (Math.round(adjustedG) << 8) + Math.round(adjustedB)).toString(16).slice(1);

    return `#${result}`;
}