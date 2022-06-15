Name: dart
Version: 2.17.1
Release: 1%{?dist}
Summary: The Dart Language
License: BSD-3-Clause
URL: https://dart.dev/

BuildArch: x86_64
Source0: https://storage.googleapis.com/dart-archive/channels/stable/release/%{version}/sdk/dartsdk-linux-x64-release.zip

%description
Dart is a client-optimized language for fast apps on any platform. This package contains the SDK used to develop and compile Dart applications.

%prep
%setup -n dart-sdk

%install
mkdir -p %{buildroot}/usr/lib/dart %{buildroot}/usr/bin
cp -r * %{buildroot}/usr/lib/dart
ln -sf /usr/lib/dart/bin/dart %{buildroot}/usr/bin/dart

%files
/usr/lib/dart
%{_bindir}/dart
%license LICENSE
%doc README