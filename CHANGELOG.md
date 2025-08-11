# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Complete GUI implementation with Tkinter
- Multi-scale template matching algorithm
- GPU acceleration support (CUDA)
- Batch processing for multiple pieces
- Real-time progress tracking and cancellation
- Export results to JSON format
- Overlap detection between pieces
- Statistical analysis of matching results

### Changed
- Improved error handling throughout the application
- Enhanced performance with downscaling options
- Better memory management for large images

### Fixed
- GUI responsiveness during long operations
- Memory leaks in image processing
- Coordinate scaling for different image sizes

## [1.0.0] - 11-08-2025

### Added
- Basic CLI interface for puzzle solving
- Image acquisition module
- Simple feature extraction
- Template matching foundation
- Project structure and documentation

### Security
- Input validation for image files
- Safe file path handling
