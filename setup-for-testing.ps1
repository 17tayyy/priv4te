# ChatGPT generated script to make a setup for testing the ranswomare
# This script generates test files in common user directories and external drives.

$UserFolders = @(
    [System.Environment]::GetFolderPath("Desktop"),
    [System.Environment]::GetFolderPath("MyDocuments"),
    [System.Environment]::GetFolderPath("MyPictures"),
    [System.Environment]::GetFolderPath("MyMusic"),
    [System.Environment]::GetFolderPath("MyVideos"),
    "$env:USERPROFILE\Downloads"
)

$ExternalDrives = Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Root -match "^[D-Z]:" } | ForEach-Object { $_.Root }
$UserFolders += $ExternalDrives

$Extensions = @(".txt", ".docx", ".xlsx", ".pdf", ".jpg", ".png", ".mp3", ".mp4", ".zip", ".csv", ".html", ".xml", ".sql")

$FileCount = 5  

foreach ($Path in $UserFolders) {
    if (Test-Path $Path) {
        Write-Host "Creating test files in: $Path"

        for ($i = 1; $i -le $FileCount; $i++) {
            $FileName = -join ((48..57) + (65..90) + (97..122) | Get-Random -Count 8 | ForEach-Object {[char]$_}) + ($Extensions | Get-Random)
            $FilePath = "$Path\$FileName"

            try {
                $Content = @(
                    "Confidential report for internal use only.",
                    "Invoice #$((Get-Random -Minimum 1000 -Maximum 9999)) - Payment confirmation.",
                    "Personal notes and important reminders.",
                    "Employee salary data (protected).",
                    "Backup file created on $(Get-Date -Format 'yyyy-MM-dd')."
                ) | Get-Random

                $Content | Out-File -Encoding UTF8 $FilePath
            }
            catch {
                Write-Host "Failed to create file in: $Path. Insufficient permissions." -ForegroundColor Red
            }
        }
    }
}

Write-Host "`nAll test files have been successfully created." -ForegroundColor Green
