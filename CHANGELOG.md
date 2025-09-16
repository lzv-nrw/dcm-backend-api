# Changelog

## [3.3.0] - 2025-09-16

### Added

- added new endpoints (read hotfolders/directories and create directory) for hotfolders to the template-API

### Removed

- deprecated `GET-/template/hotfolder-sources`

## [3.1.0] - 2025-09-11

### Changed

- added secret to response body when posting a new user-configuration

### Added

- added endpoint for revoking a user's activation status

### Removed

- removed user-activation url format string from `SelfDescription`-schema

## [3.0.0] - 2025-09-09

### Changed

- **Breaking:** updated `SelfDescription`-schema regarding new `orchestra`-package of `dcm-common`

### Removed

- **Breaking:** removed obsolete broadcast- & requeue-options in abort

## [2.5.0] - 2025-08-20

### Added

- added optional submission token to job-API
- added optional submission token to ingest-API

## [2.3.0] - 2025-08-08

### Changed

- changed `UserConfiguration.username` and `UserConfiguration.email` to optional (in requests to `PUT-/user/configure`)

### Added

- added optional query argument `templateId` to `OPTIONS-/job/configure`
- added optional query argument `group`(-identifier) to `OPTIONS-/user/configure`
- added status `"deleted"` to `UserConfiguration.status`-enum

## [2.0.0] - 2025-07-25

### Changed

- **Breaking:** refactored ingest-API and related schemas
- **Breaking:** refactored job-API and related schemas
- **Breaking:** updated SelfDescription-schema for new scheduler implementation
- **Breaking:** updated user-API schemas
- **Breaking:** replaced roles with groups-object in UserConfiguration-schema

### Added

- added initial template-API
- added initial workspace-API

## [1.0.0] - 2025-02-17

### Changed

- **Breaking:** moved `/configure` endpoints to `/job/configure`

### Added

- added user-API

## [0.1.1] - 2024-11-21

### Changed

- updated package metadata and README

## [0.1.0] - 2024-10-11

### Changed

- initial release of the dcm-backend-api
