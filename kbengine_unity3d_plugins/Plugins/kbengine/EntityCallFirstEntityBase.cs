/*
	Generated by KBEngine!
	Please do not modify this file!
	
	tools = kbcmd
*/

namespace KBEngine
{
	using UnityEngine;
	using System;
	using System.Collections;
	using System.Collections.Generic;

	// defined in */scripts/entity_defs/FirstEntity.def
	public class EntityBaseEntityCall_FirstEntityBase : EntityCall
	{

		public EntityBaseEntityCall_FirstEntityBase(Int32 eid, string ename) : base(eid, ename)
		{
			type = ENTITYCALL_TYPE.ENTITYCALL_TYPE_BASE;
		}

	}

	public class EntityCellEntityCall_FirstEntityBase : EntityCall
	{

		public EntityCellEntityCall_FirstEntityBase(Int32 eid, string ename) : base(eid, ename)
		{
			type = ENTITYCALL_TYPE.ENTITYCALL_TYPE_CELL;
		}

		public void hello(string arg1)
		{
			Bundle pBundle = newCall("hello", 0);
			if(pBundle == null)
				return;

			bundle.writeUnicode(arg1);
			sendCall(null);
		}

	}
	}
