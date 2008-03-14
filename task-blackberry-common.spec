Name:		task-blackberry-common
Version:	1.0
Release:	%{mkrel 1}
Summary:	Metapackage for charging and synchronizing Blackberry
Group:		Communications
License:	GPLv2+
Requires:	barry-charge
Requires:	barry-opensync
Suggests:	barry-gui
Suggests:	barry-tools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package for connecting with Blackberry smart
phones. It depends on the packages necessary to correctly charge
Blackberries (due to their special power requirements) and to
synchronize data using the OpenSync framework. It suggests packages
required to backup a Blackberry and to provide several small console
tools to interface with a Blackberry in various ways.

%package -n task-blackberry-kde
Summary:	KDE metapackage for synchronizing with a Blackberry
Group:		Communications
Requires:	task-blackberry-common
Requires:	libopensync-plugin-kdepim
Requires:	kdepim-kitchensync

%description -n task-blackberry-kde
This package is a meta-package for connecting with Blackberry smart
phones. It depends on all packages necessary for synchronizing with
a Blackberry using the OpenSync framework, and packages that are
useful for synchronizing with KDE applications.

%package -n task-blackberry-gnome
Summary:	GNOME metapackage for synchronizing with a Blackberry
Group:		Communications
Requires:	task-blackberry-common
Requires:	libopensync-plugin-evolution2
Requires:	multisync-gui

%description -n task-blackberry-gnome
This package is a meta-package for connecting with Blackberry smart
phones. It depends on all packages necessary for synchronizing with
a Blackberry using the OpenSync framework, and packages that are
useful for synchronizing with GNOME applications.

%files

%files -n task-blackberry-kde

%files -n task-blackberry-gnome

